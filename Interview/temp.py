
# BASE_URL = "testpage.com/"

# "employees/{keyword}" GET  200

# "employees/" GET 200

# "employees/{id}" PUT GET DELETE

# "employees/" POST 201

# def get_empployee()

def amendTheSentence(s):
    words = []
    word = s[0]

    for i in range(1, len(s)):
        if s[i].isupper():
            words.append(word)
            word = ''
            word += s[i]
        else:
            word += s[i]
    if word:
        words.append(word)

    return ' '.join([w.lower() for w in words])


s = "IForgotTheSpaces"
print(amendTheSentence(s))

if amendTheSentence("IForgotTheSpaces") == "i forgot the spaces":
    print("Passed")
if amendTheSentence("Hello") == "hello":
    print("Passed")
if amendTheSentence("VizQEogigkRZJacVELulHjG") == "viz q eogigk r z jac v e lul hj g":
    print("Passed")
if amendTheSentence("RUqOPCVENqXwvTVhpcnUtisPBt") == "r uq o p c v e nq xwv t vhpcn utis p bt":
    print("Passed")
if amendTheSentence("JhBkPBaozMnBqEWiIaOEje") == "jh bk p baoz mn bq e wi ia o eje":
    print("Passed")
