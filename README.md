# speech-recognition_practice

source : <https://github.com/Uberi/speech_recognition>

## 実行環境

- OS: windows 10
- python 3.5.4
- pocketsphinx を利用する場合は、python 3.5 まで
- Google Speech Recognition は、python 3.7 でも動くが PyAudio 最新の.whl ファイルを直接ダウンロードして pip でインストールする必要がある

### python 3.5.4

- <https://www.python.org/downloads/windows/>
- Download `Windows x86-64 executable installer`

### 必要なパッケージ (SpeechRecognition, pyaudio, pocketsphinx )

- pip install SpeechRecognition
- pip install pyaudio
- pip install pocketsphinx

### python 3.7 で動かす場合

- PyAudio 最新の.whl ファイルを直接ダウンロードして pip でインストール
- python -m pip install .\PyAudio-0.2.11-cp37-cp37m-win_amd64.whl
- 「python -m pip show pyaudio」で NumPy 等と同じ場所にちゃんとインストールされているかを確認

<https://watlab-blog.com/2019/05/21/pyaudio-install/>

## 現状

- ノイズのない wav ファイルだとうまくいく
- 自分のマイクから話したデータではとうまく認識しない(ノイズが多いのかも)
- google は多少使える
- 日本語対応は google のみ
- listen フェーズと recognition フェーズの両方とも反応が遅いため、リアルタイムでは使えない

- うまく認識しない場合は、正規表現を使うのもあり

## 参考ページ

<https://qiita.com/daiarg/items/ff1b9f91d0804e6a8f18>
