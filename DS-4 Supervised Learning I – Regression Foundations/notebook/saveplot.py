def save_plot(
    fig,
    filename,
    folder="figures",
    dpi=150,
    bbox_inches="tight"
):
    """
    Save a Matplotlib figure to disk.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        Figure to save.

    filename : str
        Output filename, e.g. "exports_over_time.png".

    folder : str, default="figures"
        Directory where the figure will be saved.

    dpi : int, default=300
        Resolution of the saved image.

    bbox_inches : str, default="tight"
        Bounding-box option used when saving.

    Returns
    -------
    str
        Path to the saved figure.
    """

    from pathlib import Path

    folder = Path(folder)
    folder.mkdir(parents=True, exist_ok=True)

    filepath = folder / filename

    fig.savefig(
        filepath,
        dpi=dpi,
        bbox_inches=bbox_inches,
        facecolor="white"
    )

    return str(filepath)
