import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

def dual_axis_plot(
    x1,
    y1,
    x2,
    y2,
    label1,
    label2,
    xlabel=None,
    ylabel1=None,
    ylabel2=None,
    title=None,
    color1="crimson",
    color2=None,
    figsize=(12, 5),
    linewidth=2,
    grid=True,
    legend1_loc="upper left",
    legend2_loc="upper center",
):
    """
    Create a publication-quality dual-axis line plot.

    Parameters
    ----------
    x1, y1 : array-like
        X and Y values for the primary y-axis.

    x2, y2 : array-like
        X and Y values for the secondary y-axis.

    label1 : str
        Legend label for the primary series.

    label2 : str
        Legend label for the secondary series.

    xlabel : str, optional
        X-axis label.

    ylabel1 : str, optional
        Primary y-axis label.

    ylabel2 : str, optional
        Secondary y-axis label.

    title : str, optional
        Plot title.

    color1 : str, default="orange"
        Color of the primary series.

    color2 : str, optional
        Color of the secondary series.

    figsize : tuple, default=(10, 5)
        Figure size.

    linewidth : float, default=2
        Width of both lines.

    grid : bool, default=True
        Whether to display grid lines.

    legend1_loc : str, default="upper left"
        Location of the primary legend.

    legend2_loc : str, default="upper center"
        Location of the secondary legend.

    Returns
    -------
    fig, ax, ax2
        Figure and both axes.
    """

    # Validate input lengths
    if len(x1) != len(y1):
        raise ValueError("x1 and y1 must have the same length.")

    if len(x2) != len(y2):
        raise ValueError("x2 and y2 must have the same length.")

    # Create figure and primary axis
    fig, ax = plt.subplots(figsize=figsize)

    # Primary axis
    ax.plot(
        x1,
        y1,
        "-",
        linewidth=linewidth,
        label=label1,
        color=color1
    )

    # Secondary axis
    ax2 = ax.twinx()

    ax2.plot(
        x2,
        y2,
        "-",
        linewidth=linewidth,
        label=label2,
        color=color2
    )

    # Axis labels
    if xlabel:
        ax.set_xlabel(xlabel, fontsize=12)

    if ylabel1:
        ax.set_ylabel(
            ylabel1,
            fontsize=12,
            color=color1
        )

    if ylabel2:
        ax2.set_ylabel(
            ylabel2,
            fontsize=12,
            color=color2
        )

    # Title
    if title:
        ax.set_title(
            title,
            fontsize=14,
            fontweight="bold",
            pad=12
        )

    # Tick styling
    ax.tick_params(
        axis="both",
        labelsize=10
    )

    ax2.tick_params(
        axis="y",
        labelsize=10
    )

    # Match tick colors to their datasets
    ax.tick_params(
        axis="y",
        labelcolor=color1
    )

    ax2.tick_params(
        axis="y",
        labelcolor=color2
    )

    # Grid
    if grid:
        ax.grid(
            True,
            linestyle="--",
            linewidth=0.7,
            alpha=0.5
        )

    # Clean spines
    ax.spines["top"].set_visible(False)
    ax2.spines["top"].set_visible(False)

    # Legends
    ax.legend(
        loc=legend1_loc,
        frameon=False
    )

    ax2.legend(
        loc=legend2_loc,
        frameon=False
    )

    # Improve layout
    fig.tight_layout()

    return fig, ax, ax2
