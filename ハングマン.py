import random

def hangman():
    word_list = ["cat", "dog", "bird","Python"]
    list_len = len(word_list) #リストの要素数を数える
    random_number = random.randint(0, list_len) #ランダムなインデックスを作る
    word = word_list[random_number] #リストのランダムなインデックスから答えを作る
    wrong = 0   #Player2の間違い回数
    stages = ["",
              "________        ",
              "|               ",
              "|       |       ",
              "|       0       ",
              "|      /|       ",
              "|      /        ",
              "|               ",
              ]

    rletters = list(word)    #wordの文字を一文字ずつ分解してリスト化
    board = ["_"] * len(word)   #wordに含まれる文字の数だけ"_"を表示
    win = False #Player2が勝ったかどうかを記録
    print("ハングマンへようこそ！")
    while wrong < len(stages) -1:   #間違えた数が(stageの要素数)より小さければ続行する
        print("\n")
        msg = "1文字を予想してね"
        char = input(msg)   #プレイヤー2の入力
        if char in rletters:    #入力文字が答えに含まれていれば当該インデックスを取得して表示を入れ替える
            cind = rletters.index(char) #当該文字のインデックス取得
            board[cind] = char  #当該インデックスを指定して答えを格納
            rletters[cind] = "$"    #同じ文字が複数あった場合にこれでループする
        else:
            wrong += 1  #入力が間違っていたら間違いの数を一つ増やす
        print(" ".join(board))  #表示用に連結して出力
        e = wrong + 1
        print("\n".join(stages[0:e]))   #現在のゲーム進行状態を表示
        if "_" not in board:    #アンダーバーが表示から消えたらプレイヤー2の勝ち
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True  #プレイヤー2の勝利判定をTrueに
            break   #ループ終了
    if not win: #win判定がFalseのままループを抜けたらプレイヤー2の負けで終了
        print("\n".join(stages[0:wrong + 1]))
        print("あなたの負け！正解は{}.".format(word))


hangman()
