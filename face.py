class face:
    def __init__(state, eyes: int, nose: int, mouth: int, chin: int) -> None:
        state.eyes = eyes
        state.nose = nose
        state.mouth = mouth
        state.chin = chin
    
    def getFaceProperties(state) -> None:
        print(state.eyes, state.mouth, state.chin, state.nose)



myFace = face(2, 1, 1, 1)
myFace.getFaceProperties()