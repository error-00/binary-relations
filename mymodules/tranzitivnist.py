def check_tranz(a1, a2, a3, i, j, k):
    res = []
    i += 1
    j += 1
    k += 1

    if a1 == 1:
        if a2 == 1:
            res.append(f'a{i} > a{j}, a{j} > a{k}')

            # Відношення
            if a3 == 1:
                res.append(f'a{i} > a{k}')
                res.append('+')
            else:
                if a3 == -1:
                    res.append(f'a{i} < a{k}')
                else:
                    res.append(f'a{i} = a{k}')
                res.append('-')

        else:
            if a2 == 0:
                res.append(f'a{i} > a{j}, a{j} = a{k}')
            else:
                res.append(f'a{i} > a{j}, a{j} < a{k}')
            res.append('транзитивність не може бути перевірено')
            res.append('')

    elif a1 == 0:
        if a2 == 0:
            res.append(f'a{i} = a{j}, a{j} = a{k}')

            # Відношення
            if a3 == 0:
                res.append(f'a{i} = a{k}')
                res.append('+')
            else:
                if a3 == -1:
                    res.append(f'a{i} < a{k}')
                else:
                    res.append(f'a{i} > a{k}')
                res.append('-')

        else:
            if a2 == 1:
                res.append(f'a{i} = a{j}, a{j} > a{k}')
            else:
                res.append(f'a{i} = a{j}, a{j} < a{k}')
            res.append('транзитивність не може бути перевірено')
            res.append('')

    else:
        if a2 == -1:
            res.append(f'a{i} < a{j}, a{j} < a{k}')

            # Відношення
            if a3 == -1:
                res.append(f'a{i} < a{k}')
                res.append('+')
            else:
                if a3 == 1:
                    res.append(f'a{i} > a{k}')
                else:
                    res.append(f'a{i} = a{k}')
                res.append('-')

        else:
            if a2 == 0:
                res.append(f'a{i} < a{j}, a{j} = a{k}')
            else:
                res.append(f'a{i} < a{j}, a{j} > a{k}')
            res.append('транзитивність не може бути перевірено')
            res.append('')

    return res
