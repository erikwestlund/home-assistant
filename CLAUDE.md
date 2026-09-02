# Home Assistant Config

Home Assistant YAML config for the house. Deployed to a live HAOS box that
controls real heating and cooling — changes here affect an occupied home.

## Deploying

The HA box checks this repo out directly at `/config`. Push here, then pull there.

**SSH access to `ha.lan` is ALLOWED, but only WITH EXPLICIT PERMISSION for that
session.** Do not connect on your own initiative, and do not treat permission
granted once as standing permission — ask again next time. When you do have it:

- `ssh ha.lan` lands as root in the `core-ssh` add-on container; config is `/config`.
- BusyBox userland: no `python3`, and `chown`/`chmod` have no `--reference`. `jq` is available.
- Back up any file before editing it, and verify afterwards (`jq -e .` for JSON).
- Restarting HA (`ha core restart`) interrupts HVAC control. Ask first.

## Reloading after a pull

Developer Tools -> YAML, **in this order** (helpers before templates, so entities
referenced by templates exist when they first render):

1. Input Booleans  2. Input Datetimes  3. Input Numbers  4. Template Entities

New files in `!include_dir_merge_*` directories are picked up by a domain reload —
the reload re-reads `configuration.yaml` and re-evaluates the includes, so no
restart is needed just to add a file. Reloading `input_number` does **not** reset
current values; it only re-clamps them to min/max.

## Gotchas

**`initial:` on `input_*` helpers is not a default — it is "force this value on
every start", and it disables state restore entirely.** HA returns early from
`async_added_to_hass` before consulting the restore store when `initial` is set.
Mnemonic: **present = frozen, absent = remembered.** The convention in this repo is
to keep it commented (`# initial: 74`) as documentation of the intended value and
set the real value in the UI. There is no "seed once then persist" in YAML.

A helper with no `initial:` and no stored state falls back to its **`min`**, not to
anything sensible. New temperature helpers therefore appear at 64°F — set them
before enabling whatever consumes them.

**The LG mini splits only accept even °F** (they store 1°C steps). See the
conversion map in `template/sensor/hvac/lg_converted_setpoints.yaml`: 75 silently
becomes 74. 77 is absent from the map and passes through unconverted — avoid it.
Where an odd setpoint is wanted, duty-cycle between two even ones across time
periods instead (see the master bedroom Sleep profile).

## Setpoint resolution

`sensor.hvac_<system>_setpoint_<room>` interpolates an entity id from two sensors:

- `sensor.hvac_comfort_setting_<room>` — period: Override / Away / Preheat / Sleep / Night / Day
- `sensor.hvac_..._comfort_setting_mode_<room>` — outdoor band: Freezing / Cold / Hot / AC

giving `input_number.hvac_<system>_<period>_<band>_setpoint_<room>`. Adding a period
therefore means adding a period sensor plus matching `input_number`s — the setpoint
template itself needs no edit. Power on/off is decided separately in
`template/binary_sensor/hvac/power_on.yaml` from `binary_sensor.hvac_daytime_active_<room>`,
so a period nested inside night needs no power-logic change.

## Dashboards

UI-managed, stored in `.storage/lovelace.dashbaord_hvac` on the box (note the typo
in that filename) and **not** in this repo — `.storage*` is gitignored. HA caches
lovelace config in memory, so editing that file requires an HA restart to take
effect, and editing the dashboard in the UI before restarting will overwrite the
file. Prefer making dashboard changes in the UI.

Per-room cards are `entities` cards gated by a `visibility` condition on
`input_select.hvac_room_settings_tabs`.
