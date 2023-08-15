from text_generation import Client

client = Client("")

if __name__ == "__main__":
    print(client.generate(
        "You are now playing as an prompter generator, given the assistant response, you shall generate a clear prompter answer for that:<|assistant|>Steven Paul Jobs (February 24, 1955 – October 5, 2011) was an American business magnate, inventor, and investor. He was the co-founder, chairman, and CEO of Apple; the chairman and majority shareholder of Pixar; a member of The Walt Disney Company's board of directors following its acquisition of Pixar; and the founder, chairman, and CEO of NeXT. He was a pioneer of the personal computer revolution of the 1970s and 1980s, along with his early business partner and fellow Apple co-founder Steve Wozniak.<|assistant|>", 
        max_new_tokens=100, temperature=0.7).generated_text
    )
