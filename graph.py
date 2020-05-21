import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

def draw_graph(event_IDs, event_count):

    y_pos = np.arange(len(event_IDs))
    plt.barh(y_pos, event_count, align='center', alpha=0.5)
    plt.yticks(y_pos, event_IDs)
    plt.xlabel('Event Count')
    plt.title('Event ID Counts')
    plt.show()
