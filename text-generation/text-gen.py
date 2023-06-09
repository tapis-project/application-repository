from transformers import pipeline


generator = pipeline("text-generation")

gen_text = ('sample sentence')

print(gen_text)

if __name__ == "__main__":
    main()