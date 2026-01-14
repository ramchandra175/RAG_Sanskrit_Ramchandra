from retriever import Retriever
from generator import Generator


def main():
    print("📥 Loading Sanskrit documents...")
    retriever = Retriever()

    print("🤖 Loading LLM (CPU)...")
    generator = Generator()

    print("\n✅ Sanskrit RAG System Ready!")
    print("Type 'exit' to quit.\n")

    while True:
        question = input("🧑‍💻 प्रश्नः: ").strip()

        if question.lower() == "exit":
            print("👋 समाप्तम्।")
            break

        context = retriever.get_context(question)

        print("\n🔍 Retrieved Context:\n")
        print(context)
        print("\n" + "-" * 50)

        answer = generator.generate(context, question)

        print("\n📜 उत्तरम्:")
        print(answer)
        print("-" * 50)


if __name__ == "__main__":
    main()
