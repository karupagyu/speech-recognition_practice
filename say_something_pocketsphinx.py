import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()

while True:
    print("Say something ...")

    with mic as source:
        r.adjust_for_ambient_noise(source)  # 雑音対策
        audio = r.listen(source)

    print("Now to recognize it...")

    # recognize speech using Sphinx
    try:
        print("Sphinx thinks you said " + r.recognize_sphinx(audio))

        # "ストップ" と言ったら音声認識を止める
        if r.recognize_sphinx(audio) == "stop":
            print("end")
            break

    # 以下は認識できなかったときに止まらないように。
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))

 