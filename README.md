# Json-Flattener
Json Flattener without handling array

## Prerequisite
- python 3.6 or above 

## How to run
Run command: ```python JsonFlattener.py```

> Supported input:
> - exit: exit the running program
> - file: choose(switch) to file(path) input mode
> - string: choose(switch) to json string input mode


1. Follow the prompt message to enter the type(json string or json file) of input data: enter ```file``` or ```string```
(you can switch later by enter **file** or **string** anytime)

2. Enter json file or string occordingly with next prompt, and repeat step 2.

3. After finish all flatten work, enter **exit** to exit the program.


Test example:
---------------
Sample Json File(Path) **Input**:
```testDir/json_test_1.json```which contains below json data:
```
{
    "a": 1,
    "b": true,
    "c": {
        "d": 3,
        "e": "test"
    }
}
```
**Output:**
```
{
    "a": 1,
    "b": true,
    "c.d": 3,
    "c.e": "test"
}
```

---------------

Sample Json String **Input**:
```
{"a1": 1, "b1": {"b2": 21, "a2": {"a3": 221, "b3": {"a4": false, "b4": {"z5": 222, "y5": true}}}, "c2": "2nd layer"}, "c1": "1st layer"}
```
**Output**:
```
{
    "a1": 1,
    "b1.b2": 21,
    "b1.a2.a3": 221,
    "b1.a2.b3.a4": false,
    "b1.a2.b3.b4.z5": 222,
    "b1.a2.b3.b4.y5": true,
    "b1.c2": "2nd layer",
    "c1": "1st layer"
}
```
