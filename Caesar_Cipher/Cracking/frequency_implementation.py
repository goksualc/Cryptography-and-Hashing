import matplotlib.pylab as plt

LETTERS = ' ABCDEFGHIJKLMNOPQRSTUVWYZ'


def frequency_analysis(text):
    text = text.upper()
    letter_frequency = {}

    for letter in LETTERS:
        letter_frequency[letter] = 0

    for letter in text:
        if letter in LETTERS:
            letter_frequency[letter] += 1

    return letter_frequency

def plot_distribution(frequencies):
    plt.bar(frequencies.keys(), frequencies.values())
    plt.xlabel('Letters')
    plt.ylabel('Frequency')
    plt.title('Letter Frequency Distribution')
    plt.show()

if __name__ == '__main__':
    plain_text = "Goksu is testing code"
    freq = frequency_analysis(plain_text)
    plot_distribution(freq)
