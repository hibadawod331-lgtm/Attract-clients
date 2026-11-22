import soundfile as sf, torch, sys
from chatterbox.mtl_tts import ChatterboxMultilingualTTS
m=ChatterboxMultilingualTTS.from_pretrained(device="cpu")
L=["ماما، رح اترك الشغل والمدرسة.","اعطوني ستة شهور، اذا ما نجحت برجع عالمدرسة.","يلا نعلم البنات كيف يعملوا نفس الشي.","من كاشيرة بسوبرماركت، لهون. ودورك انتي هلا."]
for i,t in enumerate(L):
    w=m.generate(t,language_id="ar",audio_prompt_path="ref.wav",exaggeration=0.5,cfg_weight=0.5)
    sf.write(f"line{i+1}.wav",w.squeeze().numpy(),m.sr); print('done',i+1,flush=True)
