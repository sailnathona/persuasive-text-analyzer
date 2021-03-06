from textblob import TextBlob
from math import floor
from rake_nltk import Rake


COMMON_WORDS = "hundred_words.txt"
COMMON_WORDS_THREE = "three_hundred_words.txt"


def main(split_list):
    result_polarity = polarity_check(split_list)
    result_subj = subjectivity_check(split_list)
    phrases_array = get_key_phrases(split_list)
    not_common_words_list = find_special_words(split_list)
    specials_list = not_common_words_list[1]
    result_emphasis = find_repetitions_of_words(specials_list)
    result_question = find_question_words(split_list)
    result_iwe = use_i_versus_we(split_list)
    result_avg = calculate_average_len_sentence(split_list)
    result_and = percentage_of_sentences_beginning_with_AND(split_list)
    result_you = count_yous(split_list)

    # compute total category scores
    total_pathos = (
        result_polarity[0]
        + result_subj[1]
        + not_common_words_list[2]
        + result_emphasis[1]
        + result_question[1]
        + result_iwe[1]
        + result_avg[1]
        + result_and[1]
        + result_you[0]
    )
    total_logos = (
        result_polarity[1]
        + result_subj[2]
        + not_common_words_list[3]
        + result_emphasis[2]
        + result_question[2]
        + result_iwe[2]
        + result_avg[2]
        + result_and[2]
        + result_you[1]
    )
    total_ethos = (
        result_polarity[2]
        + result_subj[3]
        + not_common_words_list[4]
        + result_emphasis[3]
        + result_question[3]
        + result_iwe[3]
        + result_avg[3]
        + result_and[3]
        + result_you[2]
    )

    print("End score for pathos is:", total_pathos)
    print("End score for logos is:", total_logos)
    print("End score for ethos is:", total_ethos)

    return (
        result_iwe[0],
        result_and[0],
        result_emphasis[0],
        not_common_words_list[0],
        result_avg[0],
        phrases_array,
        result_question[0],
        result_subj[0],
        total_pathos,
        total_logos,
        total_ethos,
    )


def polarity_check(split_list):
    """
    The sentiment property returns a namedtuple of the form Sentiment(polarity, subjectivity).
    The polarity score is a float within the range [-1.0, 1.0]
    where 1 is the most positive statement value and -1 the negative.
    The subjectivity score is a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective.
    """
    param_weights_polarity = {"pathos": 0.5, "logos": 0.3, "ethos": 0.2}
    count = 0
    polarity = 0
    for item in split_list:
        new = TextBlob(item)
        polarity += new.sentiment.polarity
        count += 1
    average_pol = polarity / count

    if -0.2 < average_pol < 0.2:
        print(
            "\nResult of polarity sentiment analysis is:", average_pol, ":- neutral\n"
        )
        pathos = 20
        logos = 20
        ethos = 20
    else:
        pathos = 7
        logos = 7
        ethos = 7
    pathos_end = pathos * param_weights_polarity["pathos"]
    logos_end = logos * param_weights_polarity["logos"]
    ethos_end = ethos * param_weights_polarity["ethos"]

    return pathos_end, logos_end, ethos_end


def get_key_phrases(split_list):
    r = Rake()
    text_string_form = " ".join(split_list)
    r.extract_keywords_from_text(text_string_form)
    keywords = r.get_ranked_phrases()[0:10]
    print(keywords)

    return keywords


def subjectivity_check(split_list):
    param_weights_subj = {"pathos": 0.5, "logos": 0.3, "ethos": 0.2}
    count = 0
    subjectivity = 0
    for item in split_list:
        new = TextBlob(item)
        subjectivity += new.sentiment.subjectivity
        count += 1
    average_sub = subjectivity / count
    average_sub = floor(average_sub * 10) / 10

    print("subjectivity", average_sub)

    if 0.3 < average_sub < 0.7:
        print(
            "Result of subjectivity sentiment analysis is:",
            average_sub,
            ":- fairly neutral: neither overly subjective nor objective\n",
        )
        pathos = 20
        logos = 20
        ethos = 20
    # this could do with fine tuning for more test cases but fine for initial testing
    else:
        pathos = 7
        logos = 7
        ethos = 7
    pathos_end = pathos * param_weights_subj["pathos"]
    logos_end = logos * param_weights_subj["logos"]
    ethos_end = ethos * param_weights_subj["ethos"]

    return average_sub, pathos_end, logos_end, ethos_end


def create_list_of_words(list):
    new_list = []
    for item in list:
        words = item.split()
        for word in words:
            new_list.append(word)

    return new_list


def find_special_words(split_list):
    file = open("three_hundred_words.txt")
    param_weights = {"pathos": 0.1, "logos": 0.45, "ethos": 0.45}
    hund_list = []
    for line in file:
        new_line = line.strip()
        hund_list.append(new_line)

    full_strip_list = create_list_of_words(split_list)
    # find words in full_split_list that are not in hund_list
    # cycle through each word in strip_list. If not in hund list, add it to specials list
    specials = []
    for word in full_strip_list:
        if word not in hund_list:
            specials.append(word)
    print("Total words not in the list of 300 most common words is:", len(specials))

    percentage = (len(specials) / len(full_strip_list)) * 100
    print("This represents a percentage of:", str(round(percentage, 1)), "%")
    if percentage >= 30:
        pathos = 20
        logos = 20
        ethos = 20
    elif 15 < percentage < 30:
        pathos = 10
        logos = 10
        ethos = 10
    else:
        pathos = 0
        logos = 0
        ethos = 0
    pathos_end = pathos * param_weights["pathos"]
    logos_end = logos * param_weights["logos"]
    ethos_end = ethos * param_weights["ethos"]

    return percentage, specials, pathos_end, logos_end, ethos_end


def find_repetitions_of_words(list):
    # not in most common words
    # emphasis is impact
    param_weights = {"pathos": 0.2, "logos": 0.5, "ethos": 0.3}
    seen = set()
    dups = set()
    for word in list:
        if word in seen:
            if word not in dups:
                dups.add(word)
        else:
            seen.add(word)
    try:
        percentage = (len(dups) / len(list)) * 100
    except Exception:
        percentage = 0
    print("The percentage of uncommon words repeated", str(round(percentage, 2)), "%\n")
    if percentage >= 10:
        pathos = 20
        logos = 20
        ethos = 20
    elif 5 < percentage < 10:
        pathos = 9
        logos = 9
        ethos = 9
    else:
        pathos = 0
        logos = 0
        ethos = 0

    pathos_end = pathos * param_weights["pathos"]
    logos_end = logos * param_weights["logos"]
    ethos_end = ethos * param_weights["ethos"]
    return percentage, pathos_end, logos_end, ethos_end


def find_question_words(list):
    param_weights = {"pathos": 0.2, "logos": 0.3, "ethos": 0.5}
    result = 0
    threshold = 4

    for item in list:
        result += item.count("?")
    print("Total questions is", result)
    # pathos, logos, ethos = 0
    if result >= threshold:
        print("The speaker poses several questions:", result, "times\n")
        pathos = 10
        logos = 20
        ethos = 20
    else:
        pathos = 0
        logos = 0
        ethos = 0
    pathos_end = pathos * param_weights["pathos"]
    logos_end = logos * param_weights["logos"]
    ethos_end = ethos * param_weights["ethos"]

    return result, pathos_end, logos_end, ethos_end


def use_i_versus_we(list):
    param_weights = {"pathos": 0.7, "logos": 0.1, "ethos": 0.3}
    number_we = number_I = 0
    for item in list:
        if "we" in item or "We" in item:
            number_we += 1
        if "I" in item:
            number_I += 1
    print(number_we)
    try:
        ratio = number_I / number_we
    except ZeroDivisionError:
        ratio = 1
    print("Ratio is", ratio)
    # print("The ratio for occurrences of 'I' to 'we' is:", str(round(ratio, 2)))
    ratio_str = str(number_I) + ":" + str(number_we)
    print("The ratio for occurrences of 'I' to 'we' is:", ratio_str)

    if number_we > number_I or ratio <= 1.1:
        print("'We' is used more than 'I'\n")
        pathos = 20
        logos = 20
        ethos = 20
    else:
        print("'I' is used more than 'We'\n")
        pathos = 0
        logos = 0
        ethos = 0

    pathos_end = pathos * param_weights["pathos"]
    logos_end = logos * param_weights["logos"]
    ethos_end = ethos * param_weights["ethos"]

    return ratio_str, pathos_end, logos_end, ethos_end


def calculate_average_len_sentence(list):
    param_weights = {"pathos": 0.4, "logos": 0.3, "ethos": 0.3}
    sum = 0
    total_items = 0
    for item in list:
        item_new = item.split()
        sum += len(item_new)
        total_items += 1
    average = sum // total_items
    print("The average words per sentence is:", average)

    if average >= 30:
        print(
            "This is decidedly over the typical average length of a sentence which is 15-20 words per sentence\n"
        )
        pathos = 20
        logos = 20
        ethos = 20
    elif 15 < average < 20:
        pathos = 10
        logos = 10
        ethos = 10
    elif 0 < average < 15:
        pathos = 5
        logos = 5
        ethos = 5
    else:
        pathos = 0
        logos = 0
        ethos = 0
    pathos_end = pathos * param_weights["pathos"]
    logos_end = logos * param_weights["logos"]
    ethos_end = ethos * param_weights["ethos"]
    return average, pathos_end, logos_end, ethos_end


def percentage_of_sentences_beginning_with_AND(list):
    param_weights = {"pathos": 0.5, "logos": 0.25, "ethos": 0.25}
    total_items_beginning_and = 0
    total_items = 0

    for item in list:
        total_items += 1
        item = item.lstrip()

        if item[0:3] == "And":  # or if item.startswith("And"):
            total_items_beginning_and += 1

    percentage = int((total_items_beginning_and / total_items) * 100)
    print(
        "The percentage of total sentences beginning with 'And' is", percentage, "%\n"
    )

    if percentage >= 35:
        pathos = 20
        logos = 20
        ethos = 20
    elif 20 < percentage < 35:
        pathos = 12
        logos = 12
        ethos = 12
    else:
        pathos = 5
        logos = 5
        ethos = 5

    pathos_end = pathos * param_weights["pathos"]
    logos_end = logos * param_weights["logos"]
    ethos_end = ethos * param_weights["ethos"]

    return percentage, pathos_end, logos_end, ethos_end


def number_of_words(list):
    word_count = 0
    for item in list:
        item = item.split()
        for word in item:
            word_count += 1
    return word_count


def count_yous(split_list):
    param_weights = {"pathos": 0.7, "logos": 0.0, "ethos": 0.3}
    num_yous = len([item for item in split_list if "you know" in item or "you" in item])
    print("Total use of the word 'you' is:", num_yous, "\n")
    word_count = number_of_words(split_list)
    percentage = (num_yous / word_count) * 100

    if percentage >= 5:
        pathos = 20
        ethos = 20
        logos = 20
    elif 3 < percentage < 5:
        pathos = 15
        ethos = 15
        logos = 15
    elif 1.5 < percentage < 3:
        pathos = 7
        ethos = 7
        logos = 7
    else:
        pathos = 0
        ethos = 0
        logos = 0
    pathos_end = pathos * param_weights["pathos"]
    logos_end = logos * param_weights["logos"]
    ethos_end = ethos * param_weights["ethos"]

    return pathos_end, logos_end, ethos_end


if __name__ == "__main__":
    main()
