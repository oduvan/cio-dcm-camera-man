"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[-300.0, 200.0, 3000.0], [20, 440], [640, 480], [["x", 180], ]],
            "answer": [20, 440]
        },
        {
            "input": [[-300.0, 200.0, 3000.0], [20, 440], [640, 480], [["z", 360], [0, 0, -1000]]],
            "answer": [95, 390]
        },
        {
            "input": [[-300.0, 200.0, 3000.0], [20, 440], [640, 480], [["z", 360], ["y", 360], [0, 0, 100]]],
            "answer": [20, 440]
        }
    ],
    "Extra": [
        {
            "input": [[-300.0, 200.0, 3000.0], [20, 440], [640, 480], [[-100, 100, 0], ["z", 180]]],
            "answer": [519, 139]
        }
    ]
}
