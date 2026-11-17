import matplotlib.pyplot as plt

def style_plot(
    ax,
    title=None,
    xlabel=None,
    ylabel=None,
    zlabel = None,
    grid=True,
    remove_spines=True,
    title_size=14,
    label_size=11,
    tick_size=9,
    title_weight="bold",
):

    if ax is None:
        raise ValueError("ax cannot be None.")

    # Title and axis labels
    if title:
        ax.set_title(
            title,
            fontsize=title_size,
            fontweight=title_weight,
            pad=12
        )

    if xlabel:
        ax.set_xlabel(
            xlabel,
            fontsize=label_size,
            labelpad=8
        )

    if ylabel:
        ax.set_ylabel(
            ylabel,
            fontsize=label_size,
            labelpad=8
        )

    if zlabel:
        ax.set_zlabel(
            zlabel, 
            fontsize=label_size, 
            labelpad=8
        )

    # Tick labels
    ax.tick_params(
        axis="both",
        labelsize=tick_size
    )

    # Grid
    if grid:
        ax.grid(
            True,
            linestyle="--",
            linewidth=0.7,
            alpha=0.3
        )
    else:
        ax.grid(False)

    # Remove unnecessary spines
    if remove_spines:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

        for spine in ax.spines.values():
            spine.set_linewidth(1.2)

    # Improve layout
    ax.margins(x=0.02)

    ax.set_facecolor("whitesmoke")

    return ax
