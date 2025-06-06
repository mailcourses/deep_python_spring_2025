from collections.abc import Iterable, Sequence
from dataclasses import dataclass
from typing import (
    Any,
    TYPE_CHECKING,
    NewType,
    Generator,
    TypeVar,
    runtime_checkable,
    Protocol,
)


@dataclass
class User:
    user_id: str
    name: str
    age: int

    def __bool__(self):
        return self.user_id in {"123", "a1w3"}


@dataclass
class LibraryAccount(User):
    pass


type UserData = dict[str, str | int]
type OptUserData = UserData | None


def fetch_user(user_id: str) -> UserData:
    return {
        "user_id": user_id,
        "name": "Steve",
        "age": 99,
    }


def get_user_data(user: User) -> OptUserData:
    if not user:
        return None

    data = fetch_user(user.user_id)

    return data


def run_get_user_data() -> None:
    user = User("123", "Steve", 99)
    res: OptUserData = get_user_data(user)
    print(f"1: get_user_data={res}")

    user = LibraryAccount("a1w3", "Lib", 105)
    res = get_user_data(user)
    print(f"2: get_user_data={res}")

    user = User("not_a_user", "Steve", 99)
    res = get_user_data(user)
    print(f"3: get_user_data={res}")


Celsius = NewType("Celsius", float)
Fareng = NewType("Fareng", float)


def convert_c_to_f(temp: Celsius) -> Fareng:
    return Fareng(temp * 9 / 5 + 32)


def gen_celsius_temps(start: Celsius) -> Generator[Celsius, None, str]:
    yield start
    yield Celsius(start + 10)
    yield Celsius(start + 20)

    return "gen finished"


@runtime_checkable
class Comparable(Protocol):
    def __lt__(self: "T", other: "T") -> bool: ...
    def __gt__(self: "T", other: "T") -> bool: ...


T = TypeVar("T", bound=Comparable)

def get_max_temp(temps: Iterable[T]) -> T | None:
    if not temps:
        return None

    return max(temps)


# def get_max_temp(temps: Iterable[Celsius]) -> Celsius | None:
#     if not temps:
#         return None
#
#     return max(temps)


def get_first_temp[V](temps: Sequence[V]) -> V | None:
    if not temps:
        return None

    return temps[0]


def run_temperatures() -> None:
    temp_c = Celsius(36.6)
    temp_f = convert_c_to_f(temp_c)
    print(f"1: {temp_c=}, {temp_f=}, {type(temp_c)}")

    temp_c = Celsius(-40)
    temp_f = convert_c_to_f(temp_c)
    print(f"2: {temp_c=}, {temp_f=}, {type(temp_c)}")

    temps: Iterable[Celsius] = [Celsius(36.6), Celsius(-40)]
    max_temp = get_max_temp(temps)
    print(f"3: {max_temp=}, {temps=}")

    temps = gen_celsius_temps(Celsius(10))
    max_temp = get_max_temp(temps)
    print(f"4: {max_temp=}, {temps=}")

    temps_seq: Sequence[Celsius] = [Celsius(36.6), Celsius(-40)]
    first_temp = get_first_temp(temps_seq)
    print(f"5: {first_temp=}, {temps_seq=}")

    temps_1: tuple[Celsius, ...] = (Celsius(36.6), Celsius(-40), Celsius(0))
    first_temp = get_first_temp(temps_1)
    print(f"6: {first_temp=}, {temps_1=}")

    temps_int = [36, -40, 50]
    max_temp7 = get_max_temp(temps_int)
    print(f"7: {max_temp7=}, {temps_int=}")

    first_temp1: int | None = get_first_temp(temps_int)
    print(f"8: {first_temp1=}, {temps_int=}")


@runtime_checkable
class Predictable(Protocol):
    def predict(self) -> float:
        pass


class RandomForest:
    def predict(self) -> float:
        return 0.95


def calc_prediction(model: Predictable) -> float:
    #return model.predict()
    return 0.1


def run_predictable() -> None:
    model = RandomForest()
    score = calc_prediction(model)
    print(f"{score=}")

    user = User("123", "Steve", 99)
    print(f"{isinstance(model, Predictable)=}, {isinstance(user, Predictable)=}")

    score = calc_prediction(user)
    print(f"{score=}")


if __name__ == "__main__":
    print(issubclass(Iterable, Sequence), issubclass(Sequence, Iterable))

    print(f"{TYPE_CHECKING=}")
    run_get_user_data()

    print()
    run_temperatures()

    print()
    run_predictable()

    print("ok")
