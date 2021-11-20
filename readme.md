# Python 2*2 Puzzle Game

## Please find the executable file in the `/dist` named `puzzle.exe` folder.

![Program Menu](https://lh3.googleusercontent.com/U58aJIv51YVnLE6uY-qoelBlA046go6QDygGXXQHi9RhfQqXiekh7upUiWcQbkbqgJsPZfKdamQdsSzsIHZDhKhf9cuNhzHyqkXxX7uAXxCJP-0thLsShY5rJKwRdm9OPQReVUq9nxFrTZYPSCoJKTgeZ650zp27ZVEg73uxHKe_V1OZndpJuzti8967hdUoTIuig4a6qxq_LyyQa4H3IUrHgO92NBqD3VxDFkfGRUPQ9RsN60of39-2kdrdZHdYn287DTN_BYCZs_6kvgf-WJ5iSPf1nX0Cljqv4yg8_mqLXIYb9M5auCe6n7N6_NQYGHfrzSRDOTk2l1fkM4_m7AFGzE604CSale2W0P-GoN-bBjYSU9iiQgXUNQmXehqW7WSFlaDbqlIgt7YYbNn1OW8pB6eelItjNzpBmdlefcye0HTiRXxKOc8giSM0Aox7osEaTvYNFhK1ZdHT2ydDe7Ajqg0RqQlHbEzyMpdKPA1iy0hAMHAZbRGKIdo4dw6IKJNsMvSO5xEGr5vXsJfWzOFwK881w4dC78qv8WWZnf9J1r9wV-maFUCYdsOnhMF5NW0d47SP-o5zg0GN0wD832P-SfdrWGEWFcfPGIz7xHwjqFBvhl_ioq-f_4gIVsUMcs_YAzJupYc7ClhImxIg-hlbA5ly-jfkL82vQJRk-_g391d0mcmdXOoPvfyaCLjEQQfgJFMNY7dAiXJWbPzkYdc=w268-h243-no?authuser=0)
The program takes two inputs of `initialState` and `goalState`. In the above listed diagram the `initialState=[1,2,0,3]` and the final/goal/desired state is `goalState=[1,2,3,0]`. 
*Here 0 represents the spared/extra area in the puzzle. The area to which a block can be moved.*
The program uses the `Breadth First Search` approach to generate the whole game tree to find the given desired state for the puzzle.
