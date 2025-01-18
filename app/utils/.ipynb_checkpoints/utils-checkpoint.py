import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML

def get_false_predictions(all_models):
    misclassed_index = []
    for i in all_models.values:
        m = np.where(i[0] != i[1])
        for j in m[0]:misclassed_index.append(j)
    return sorted(misclassed_index)

def plot_hist(history):
    plt.figure(figsize=(8,3))

    plt.subplot(1,2,1)
    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title('Accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'])
    
    plt.subplot(1, 2, 2)
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('Loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'])
    plt.show()

# @source https://docs.seldon.io/projects/alibi/en/latest/examples/integrated_gradients_imdb.html
def hlstr(string, color='white'):
    """
    Return HTML markup highlighting text with the desired color.
    """
    return f"<mark style=background-color:{color}>{string} </mark>"

# @source https://docs.seldon.io/projects/alibi/en/latest/examples/integrated_gradients_imdb.html
def colorize(attrs, cmin, cmax, cmap='RdYlGn'):
    """
    Compute hex colors based on the attributions for a single instance.
    Uses a diverging colorscale by default and normalizes and scales
    the colormap so that colors are consistent with the attributions.
    """
    # cmap_bound = np.abs(attrs).max()
    norm = mpl.colors.Normalize(vmin=cmin, vmax=cmax)
    cmap = mpl.colormaps[cmap]

    # now compute hex values of colors
    colors = list(map(lambda x: mpl.colors.rgb2hex(cmap(norm(x))), attrs))
    return colors

# @source https://docs.seldon.io/projects/alibi/en/latest/examples/integrated_gradients_imdb.html
def decode_sentence(x, reverse_index):
    return " ".join([reverse_index.get(i, '') for i in x])
    