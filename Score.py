import Utils


def add_score(difficulty):
    points_of_winning = ((difficulty * 3) + 5)
    try:
        f1 = open(Utils.score_file_name, "r")
        current_score = int(f1.readline())
        f1.close()
        f2 = open(Utils.score_file_name, "w")
        score_to_add = str(current_score + points_of_winning)
        f2.write(score_to_add)
        f2.close()
    except:
        file = open(Utils.score_file_name, "w")
        score_to_add = str(points_of_winning)
        file.write(score_to_add)
        file.close()

