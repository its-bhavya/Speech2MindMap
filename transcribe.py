import whisper
import time

start = time.time()
model1 = whisper.load_model("base")
result1 = model1.transcribe("delme_rec_unlimited_bx12bbjl.wav")
print(result1)
end = time.time()
print((end-start)*10**3 ,"ms")

start = time.time()
model2 = whisper.load_model("medium")
result2 = model2.transcribe("delme_rec_unlimited_bx12bbjl.wav")
print(result2)
end = time.time()
print((end-start)*10**3 ,"ms")
