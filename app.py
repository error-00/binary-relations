from flask import Flask, render_template, request
from mymodules.tranzitivnist import check_tranz
import operator

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/names', methods=['GET', 'POST'])
def names():
    n = int(request.args.get('n'))
    if request.method == 'POST':
        names = [request.form.get(f'name_{i}') for i in range(n)]
        return render_template('matrix.html', n=n, names=names)
    return render_template('names.html', n=n)


@app.route('/matrix/', methods=['GET', 'POST'])
def matrix():
    n = int(request.form['n'])
    names = request.form.getlist('names')
    # Перевірка на унікальність введених імен об'єктів
    if len(names) != len(set(names)):
        error = "Імена об'єктів повинні бути унікальними!"
        return render_template('names.html', n=n, error=error)
    return render_template('matrix.html', n=n, names=names)


@app.route('/result/', methods=['GET', 'POST'])
def result():
    n = int(request.form['n'])
    names = request.form.getlist('names')
    matr = request.form.getlist('matrix')
    matrix = []

    # Створення вкладених списків у списку
    for i in range(0, len(matr), n):
        matrix.append(matr[i:i + n])

    # Змінюємо елементи нижньої трикутної матриці
    for i in range(n):
        for j in range(n):
            if i > j:
                matrix[i][j] = -int(matrix[j][i])
            elif i == j:
                matrix[i][j] = 0
            else:
                matrix[i][j] = int(matrix[i][j])

    # створюємо словник для сум об'єктів
    sum_dict = {}
    for i, obj in enumerate(names):
        row = matrix[i]
        sum_dict[obj] = sum([int(x) for x in row])

    # Сортуємо словник
    sorted_tuples = sorted(sum_dict.items(), key=operator.itemgetter(1), reverse=True)
    sorted_dict = {k: v for k, v in sorted_tuples}

    ranj_str = ''
    ctn = 0
    flag_key = 0

    # Ранжування
    for key in sorted_dict.keys():
        if ctn == 0:
            ranj_str += key
            ctn += 1
        else:
            if sorted_dict[flag_key] > sorted_dict[key]:
                ranj_str += ' > '
            else:
                ranj_str += ' = '
            ranj_str += key
        flag_key = key

    # Перевірка на транизитивність
    comb = []
    cond_tranz = []
    vidnosh = []
    prim = []

    for i in range(1, n - 1):
        for j in range(i + 1, n):
            for k in range(j + 1, n + 1):
                comb.append([f'a{i}', f'a{j}', f'a{k}'])
                res = check_tranz(matrix[i - 1][j - 1], matrix[j - 1][k - 1], matrix[i - 1][k - 1], i - 1, j - 1, k - 1)
                cond_tranz.append(res[0])
                vidnosh.append(res[1])
                prim.append(res[2])

    # Розпаковка вкладених списків комбінацій
    for i in range(len(comb)):
        comb[i] = ', '.join(comb[i])

    # Висновок
    if prim.count('-') >= 1:
        visnovok = f'Перевірка на транзитивність показала, що у {prim.count("-")} випадках з {prim.count("-") + prim.count("+")} можливих для перевірки транзитивність була порушена. Це означає, що експерт у своїх оцінках був непослідовним. '
    else:
        visnovok = 'Перевірка на транзитивність показала, що транзитивність жодного разу не була порушена. Це означає, що експерт у своїх оцінках був послідовним.'

    return render_template('result.html', n=n, names=names, matrix=matrix, sorted_dict=sorted_dict,
                           ranj_str=ranj_str, comb=comb, len_comb=len(comb), cond_tranz=cond_tranz,
                           vidnosh=vidnosh, prim=prim, visnovok=visnovok)


if __name__ == '__main__':
    app.run(debug=True)
