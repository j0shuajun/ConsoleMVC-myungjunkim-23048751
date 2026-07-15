"""Reads user input, updates the Model, and calls the View."""

import view
from model import Sample, SampleModel


def register_sample(model):
    sample_id, name, average_production_time, yield_rate = view.prompt_sample_input()
    if model.find(sample_id) is not None:
        view.show_duplicate_error(sample_id)
        return
    sample = Sample(sample_id, name, average_production_time, yield_rate)
    model.add(sample)
    view.show_registered(sample)


def list_samples(model):
    view.show_sample_list(model.list_all())


def run(model=None):
    model = model or SampleModel()
    while True:
        view.show_main_menu()
        choice = view.prompt_choice()
        if choice == "1":
            register_sample(model)
        elif choice == "2":
            list_samples(model)
        elif choice == "0":
            view.show_goodbye()
            break
        else:
            view.show_unknown_choice()
