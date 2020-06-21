import json
import sys, traceback

class JsonFlattener:
    def flatten(self, jsonObject):
        jsonOutput = {}
        
        # dfs the nested json structure
        def dfs(para, prefix = ""):
            if type(para) is dict:
                # If there is nested structure inside of para
                for field in para:
                    dfs(para[field], prefix + field + '.')
            else:
                # There is no nested structure inside of para
                jsonOutput[prefix[:-1]] = para

        dfs(jsonObject)
        return jsonOutput

def main():
    print("Hello from Json Flattener!")
    print ("Enter 'exit' to exit json flattener")

    jf = JsonFlattener()
    supportedInputSource = ["file", "string"]

    # Choose the input source
    choice = ""
    while choice not in supportedInputSource:
        if choice == "exit":
            break
        choice = input('\nPlease enter what type of json you want use as input (enter *file* or *string*) \n \
        (you can switch later by enter *file* or *string* anytime)\n')

    jsonObject = None
    while True and choice in supportedInputSource:
        # Enter input data
        try:
            if choice == "file":
                filePath = input('\nPlease enter the file path:\n')
                if filePath == "exit":
                    break
                elif filePath == "string":
                    choice = "string"
                    print ("Switch input source to json **string**")
                    continue
                with open(filePath, "r") as content:
                    jsonObject = json.load(content)
            elif choice == "string":
                jsonString = input('\nPlease enter the jsonString here: (Ex. {"a": 1})\n')
                if jsonString == "exit":
                    break
                elif jsonString == "file":
                    choice = "file"
                    print ("Switch input source to json **file**")
                    continue
                jsonObject = json.loads(jsonString)

            print("Flattened json:")
            flattenedJson = jf.flatten(jsonObject)
            print (json.dumps(flattenedJson, indent=4))
        except json.decoder.JSONDecodeError as jsonError:
            print ("Input json format is not correct, please try again.")
        except Exception as ex:
            print ("!!!Something went wrong!!!")
            traceback.print_exc(file=sys.stdout)

    print ("Exited")


if __name__ == "__main__":
    main()
