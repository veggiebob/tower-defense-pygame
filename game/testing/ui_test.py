from game.common.yaml_parsing import YAMLInstancer
yaml_layout = """
start_screen:
  class: &panel game.subsystems.ui.layout.panel@Panel
  orientation: vertical
  intended_window: [0, 0, 1, 1]
  x: 0
  y: 0
  width: 2.0
  height: 2.0
  inner_panels:
    - class: *panel
      x: 0
      y: 0
      height: 0.5
      width: 1.0
    - class: *panel
      x: 0
      y: 0.5
      width: 1.0
      height: 0.5
      inner_panels:
      - class: *panel
        x: 0
        y: 0
        width: 0.5
        height: 1.0
      - class: *panel
        x: 0.5
        y: 0
        width: 0.5
        height: 1.0
"""

panel = YAMLInstancer.get_single(yaml_layout)
print(panel)
inner_panels = panel.get_all_inner()
print('flattened layout:')
print('; '.join([str(p) for p in inner_panels]))