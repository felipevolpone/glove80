# zmk-glove80

ZMK config for the MoErgo Glove80, ported from my Charybdis 4x6 layout
([`~/p/zmk-charybdis`](../zmk-charybdis)). Same layers, same home row mods,
same combos; the extra Glove80 keys (F-row, bottom row, second thumb arc)
carry over from my previous Glove80 layout.

Firmware is MoErgo's ZMK fork ([moergo-sc/zmk](https://github.com/moergo-sc/zmk)),
built with nix exactly like the official
[glove80-zmk-config](https://github.com/moergo-sc/glove80-zmk-config) template.

## Layers

Hold a thumb key to reach a layer. Left T4/T5/T6 and right T4/T5/T6 are the
lower thumb arc (T4 = resting position).

| Thumb     | Left hand             | Right hand              |
|-----------|-----------------------|-------------------------|
| T4        | Space / hold: SYM     | Backspace / hold: NAV   |
| T5        | Esc / hold: NAV       | Enter / hold: NUM       |
| T6        | LGUI / hold: MOUSE    | Cmd+` (cycle windows)   |
| T1        | sticky RGUI           | RShift                  |
| T2        | LCtrl                 | RCtrl                   |
| T3        | LAlt                  | Magic (hold) / RGB status (tap) |

### Base

```
 Cmd+Spc  F2   F3   F4   F5                                  F6   F7   F8   F9   F10
   `      1    2    3    4    5                         6     7    8    9    0    -
  Tab     Q    W    E    R    T                         Y     U    I    O    P    \
 Shift  A/Cmd S/Alt D/Sft F/Ctl G                       H  J/Ctl K/Sft  L  ;/Cmd  '
  RGUI    Z    X    C    V    B   sRGUI Ctrl Alt  Magic Ctrl Sft  N     M    ,    .    /   PgUp
  Ctrl  Home  End   ←    →      Spc/SYM Esc/NAV Gui/MOU  Cmd+` Ent/NUM Bsp/NAV  ↑    ↓    [    ]   PgDn
```

Home row mods are urob's "timeless" HRMs (same settings as `~/p/totem`):
balanced flavor, 240 ms tapping term, 140 ms quick-tap, 150 ms require-prior-idle,
hold-trigger-on-release, triggered only by the opposite hand and the thumbs.

### NAV (hold left Esc or right Backspace)

```
                Cmd+[ Cmd+]  Cmd+{ Cmd+}          CapsWord Alt+←  Alt+→
              Vol-  Mute   Vol+                    0       Alt+←  Alt+→  Cmd+Shift+J
                   Play  Cmd+←  Cmd+→              CapsLock Cmd+Shift+4
      Shift+Enter (on Space)
```

### SYM (hold Space)

```
   `    -    {    }    !            *    $    %    '    "
   ~    +    (    )    @            ←    ↓    ↑    →    ;
   |    _    [    ]    #            :    =    &    \    Ctrl
                                            Alt+Bsp (on Backspace)
```

### NUM (hold Enter)

```
   1    2    3    4    5
   6    7    8    9    0
   +    -    *    /    :                              bootloader (right half, top-right `-` key)
```

### MOUSE (hold left LGUI thumb)

The Charybdis has a trackball; here the layer drives the pointer from the keys.

```
             scroll↑ scroll↓ (D F)          ←  ↓  ↑  →  (H J K L)
   bootloader (left half, top-left ` key)
   thumbs: LClick RClick  ·   MClick RClick LClick
```

### MAGIC (hold right T3)

Stock Glove80 layer: BT profiles (`bt_0`..`bt_3` on the left thumbs), BT clear,
RGB controls, `&bootloader` on both home-row outer keys, `&sys_reset` on both
bottom-row outer keys, USB output.

## Combos (right home row)

| Keys      | Action                              |
|-----------|-------------------------------------|
| H + J     | Shortcat (Cmd+Alt+Shift+S)          |
| J + K     | tmux previous window (Ctrl+A, H)    |
| K + L     | tmux next window (Ctrl+A, N)        |
| J + K + L | Raycast notes (Ctrl+Alt+Shift+Cmd+Space) |

## Building

**GitHub Actions**: push to GitHub and the `Build` workflow uploads
`glove80.uf2` as an artifact. It checks out `moergo-sc/zmk@main`; pin `ref`
in `.github/workflows/build.yml` to a release tag (e.g. `v25.11`) if needed.

**Locally** (needs nix):

```sh
./build.sh          # clones moergo-sc/zmk into ./src on first run, writes glove80.uf2
```

Before pushing, run the layer sanity check:

```sh
python3 scripts/check-keymap.py
```

## Flashing

`glove80.uf2` contains both halves. For each half: hold Magic + the bootloader
key (or double-tap the reset button), copy the file onto the `GLV80LHBOOT` /
`GLV80RHBOOT` drive. Flash the left half first if you change bluetooth settings.

## Differences from the Charybdis

- No trackball, so MOUSE gets `&mmv` on HJKL and click keys on both thumb clusters.
- Extra Glove80 keys: F-row (F1 replaced by Cmd+Space, as before), `\` and
  PgUp/PgDn on the right outer column, Home/End/arrows/brackets on the bottom row,
  plain modifiers on the upper thumb arc.
- The Charybdis `&mkp LCLK` on the lower-left thumb has no counterpart.
