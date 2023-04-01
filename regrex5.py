import random
import re
import string

def generate_random_text(length=100):
    text = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return text

def choose_random_question(questions, n=2):
    return random.sample(questions, n)

def test_regex(regex, answer, text):
    result = re.findall(regex, text)
    if result == answer:
        return True, result 
    else:
        return False, result

def main():
    questions = [
        ("請匹配所有的大寫字母", r'[A-Z]', lambda x: [c for c in x if c.isupper()]),
        ("請匹配所有的小寫字母", r'[a-z]', lambda x: [c for c in x if c.islower()]),
        ("請匹配所有的數字", r'\d', lambda x: [c for c in x if c.isdigit()]),
        ("請匹配字母和數字字符之間的空格", r'(?<=\w)\s(?=\w)', lambda x: [' ' for _ in range(len(re.findall(r'\w\s\w', x)))]),
        ("請匹配文本開始的3個字符", r'^.{3}', lambda x: [x[:3]]),
        ("請匹配所有的連續3組數字", r'\d{3}', lambda x: re.findall(r'\d{3}', x)),
        ("請匹配連續的2到4個數字", r'\d{2,4}', lambda x: re.findall(r'\d{2,4}', x)),
        ("請匹配以字母開始的3個字母組合", r'(?<=\b)[a-zA-Z]{3}(?=\b|\d)', lambda x: re.findall(r'\b[a-zA-Z]{3}(?=\b|\d)', x)),
        ("請匹配電子郵件地址", r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', lambda x: re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', x)),
        ("請匹配文本結尾的3個字符", r'.{3}$', lambda x: [x[-3:]]),
    ]
    
    text = generate_random_text()
    print(f"隨機文本為: {text}")

    while True:
        combined_question = choose_random_question(questions)
        operator_sample = random.choice(['AND', '同时满足'])

        if operator_sample == 'AND':
            condition_text = " AND ".join(f"({q[0]})" for q in combined_question)
            user_regex = ''.join(f"({q[1]})" for q in combined_question)
            combined_answer = [val for q in combined_question for val in q[2](text)]
        else: # 同时满足
            condition_text = f"同时满足以下条件:\n - {combined_question[0][0]}\n - 在上述结果中，{combined_question[1][0]}"
            user_regex = f"{combined_question[0][1]}(?={combined_question[1][1]})"
            combined_answer = re.findall(user_regex, text)

        print(f"請匹配符合以下條件的字串：\n{condition_text}")

        while True:
            user_regex_input = input("請輸入正規表達式：")
            
            if user_regex_input == "":
                print(f"建議的正則表達式：{user_regex}")
                user_regex_input = user_regex
            
            is_correct, result = test_regex(user_regex_input, combined_answer, text)
            
            if is_correct:
                print(f"正確! 匹配結果為: {result}")
                print("Pass")
                break
            else:
                print(f"錯誤! 匹配結果為: {result}")

        if input("是否繼續？(是/否)：").lower() == '否':
            break

if __name__ == "__main__":
    main()
