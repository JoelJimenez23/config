
from libqtile import layout
from libqtile.config import Match


layouts = [
    layout.Columns(margin = 15,border_focus="#bb6663",border_width=0,border_normal="#00000000"),
    layout.Max()
]

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    border_focus="#00000000",
    border_normal="#00000000"
)
