from kfp import dsl, compiler

@dsl.component()
def first_pipeline() -> str:
    print("Hello First World!")

    return "first"

@dsl.component()
def second_pipeline() -> str:
    print("Hello Second World!")

    return "second"

@dsl.pipeline()
def my_pipeline():
    resp1 = first_pipeline()
    resp2 = second_pipeline()


if __name__ == "__main__":
    compiler.Compiler().compile(my_pipeline, "basic.yaml")
