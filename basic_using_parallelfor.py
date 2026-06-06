from kfp import dsl, compiler

@dsl.component()
def first_pipeline(message: str) -> str:
    print(f"Hello {message} World!")

    return message


@dsl.pipeline()
def my_pipeline():
    items = ["a", "b", "c", "d"]

    with dsl.ParallelFor(items) as item:
        first_pipeline(message=item)


if __name__ == "__main__":
    compiler.Compiler().compile(my_pipeline, "basic_using_parallelfor.yaml")
