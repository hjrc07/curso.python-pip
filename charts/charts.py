import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [200, 34, 120]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    #plt.show() Para mostrar en consola
    plt.savefig('pie.png')    #Para guardar en imagen
    plt.close()