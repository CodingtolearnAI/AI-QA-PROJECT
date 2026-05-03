def print_report(prompt, result):
    print("\n=======================")
    print(f"Prompt: {prompt}")
    print(f"Score: {result['score']}/3")


    if result["errors"]:
        print("Status = Fail")
        for error in result["errors"]:
            print(f"- {error}")
    else:
        print("Status = Pass")