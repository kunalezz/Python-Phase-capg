class Solution:
    def quiz_score(self, student, correct):
        score = 0
        for i in range(0, len(student)):
            if student[i] == correct[i]:
                score += 5
            elif student[i] == "X":
                continue
            else:
                score -= 2

        percentage = (score / len(correct) * 5) * 100
        if percentage >= 70:
            score += 10           
        return score