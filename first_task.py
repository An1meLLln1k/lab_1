def read_file():
    with open("./data/first_task.txt", encoding="utf-8") as file:
        return file.readlines()

def text_to_words(lines):
    words = []

    for line in lines:
        _line = (line
            .replace("'", "")
            .replace("?", "")
            .replace("!", "")
            .replace(",", "")
            .replace(".", "")
            .replace("-", "")
            .lower().strip())
        words += _line.split(" ")
    return  words

def calc_freq(words):
    word_freq = {}
    for word in words:
        if len(word) == 0:
            continue
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

def write_to_file(stat):
    with open("first_task_result.txt", "w", encoding="utf-8") as file:
        for key, val in stat:
            file.write(f"{key}:{val}\n")

def average_sentences_per_paragraph(lines):
    paragraphs = [line for line in lines if line.strip()]  # Убираем пустые строки (абзацы)
    sentence_counts = [len([s for s in paragraph.split('.') if s.strip()]) for paragraph in paragraphs]
    average_sentences = sum(sentence_counts) / len(sentence_counts) if sentence_counts else 0
    return average_sentences

def write_paragraph_analysis(avg_sentences):
    with open("first_task_result2.txt", "w", encoding="utf-8") as file:
        file.write(f"Среднее количество предложений в абзацах: {avg_sentences:.2f}\n")

lines = read_file()
words = text_to_words(lines)
word_freq = calc_freq(words)
write_to_file(word_freq)

average_sentences = average_sentences_per_paragraph(lines)
write_paragraph_analysis(average_sentences)
