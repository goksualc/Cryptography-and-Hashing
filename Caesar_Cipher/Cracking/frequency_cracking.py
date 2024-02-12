import matplotlib.pylab as plt

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # Adjusted the alphabet string


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
    plt.show()

def caesar_crack(text):
    freq = frequency_analysis(text)
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)  # Fixed sorting key
    print("The possible key value: %s" % (LETTERS.find(freq[0][0]) -
                                           LETTERS.find('E')))
    # plot_distribution(freq)  # Uncomment this line if you want to plot the distribution


if __name__ == '__main__':
    cipher_text = "Ksowymwxiwxmrkgshi"
    caesar_crack(cipher_text)
