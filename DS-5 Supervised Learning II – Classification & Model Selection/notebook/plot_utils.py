import matplotlib.pyplot as plt
import seaborn as sns

def style_plot(
    ax,
    title=None,
    xlabel=None,
    ylabel=None,
    figsize=None,
    grid=True,
    remove_spine=True,
    spine_width=1.2,
    label_fontsize=11,
    title_fontsize=13
):
    if figsize:
        ax.figure.set_size_inches(*figsize)

    if xlabel:
        ax.set_xlabel(xlabel, fontsize=label_fontsize)

    if ylabel:
        ax.set_ylabel(ylabel, fontsize=label_fontsize)

    if title:
        ax.set_title(
            title,
            fontsize=title_fontsize,
            fontweight="bold"
        )

    if grid:
        ax.grid(alpha=0.3)

    if remove_spine:
        sns.despine(ax=ax, top=True, right=True)

    # Set spine width
    for spine in ax.spines.values():
        spine.set_linewidth(spine_width)

    return ax