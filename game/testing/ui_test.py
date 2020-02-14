from game.common.yaml_parsing import YAMLInstancer
yaml_layout = """
start_screen:
  class: &layout game.subsystems.ui.layout.layout@Layout
  orientation: vertical
  intended_window: [0, 0, 1, 1]
  inner_panels:
    - top:
        class: &panel game.subsystems.ui.layout.panel@Panel
        weight: 0.5
    - bottom:
        class: *panel
        weight: 0.5
"""

layout = YAMLInstancer.get_single(yaml_layout)
print(layout)