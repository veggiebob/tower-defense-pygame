from game.common.yaml_parsing import YAMLInstancer
yaml_layout = """
start_screen:
  class: &panel game.subsystems.ui.layout.panel@Panel
  orientation: vertical
  intended_window: [0, 0, 1, 1]
  inner_panels:
    - top:
        class: *panel
        x: 0
        y: 0
        height: 0.5
        width: 1.0
    - bottom:
        class: *panel
        x: 0
        y: 0.5
        width: 1.0
        height: 0.5
"""

panel = YAMLInstancer.get_single(yaml_layout)
print(panel)
panels = panel.get_all_inner()
print(panels)