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
    """
    Apply consistent, publication-quality styling to a Matplotlib Axes.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The Axes object to style.

    title : str, optional
        Plot title.

    xlabel : str, optional
        X-axis label.

    ylabel : str, optional
        Y-axis label.

    grid : bool, default=True
        Whether to display grid lines.

    remove_spines : bool, default=True
        Whether to remove the top and right spines.

    title_size : int, default=16
        Font size of the title.

    label_size : int, default=12
        Font size of axis labels.

    tick_size : int, default=10
        Font size of tick labels.

    title_weight : str, default="bold"
        Font weight of the title.

    Returns
    -------
    matplotlib.axes.Axes
        The styled Axes object.
    """

    if ax is None:
        raise ValueError("ax cannot be None.")

    # Background
    ax.set_facecolor("white")

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

    # Improve layout
    ax.margins(x=0.02)

    return ax
