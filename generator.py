import random
from workflowhub import WorkflowGenerator
from workflowhub.generator import EpigenomicsRecipe, GenomeRecipe, MontageRecipe, CyclesRecipe, SoyKBRecipe, \
    SeismologyRecipe
import os

workflow_size_cat1 = {1: 100, 2: 200, 3: 500, 4: 1000}
workflow_size_cat2 = {1: 50, 2: 100, 3: 200, 4: 1000}
workflow_size_cat3 = {1: 50, 2: 100, 3: 200, 4: 500, 5: 1000}
all_workflow_types = {1: EpigenomicsRecipe, 2: GenomeRecipe, 3: MontageRecipe, 4: CyclesRecipe, 5: SoyKBRecipe}
path_dict = {"s": "WorkflowHubSmallWorkload", "m": "WorkflowHubMediumWorkload", "l": "WorkflowHubLargeWorkload"}

workflow_size_dict = workflow_size_cat3
path = path_dict.get("s")  # /WorkflowHubSmallWorkload /WorkflowHubMediumWorkload /WorkflowHubLargeWorkload
total_workflow_number = 1000  # 1000, 2000, 4000

if not os.path.exists(path):
    os.mkdir(path)
    for i in range(total_workflow_number):
        chosen_Recipe_class = all_workflow_types.get(random.randint(1, 5))

        if chosen_Recipe_class == SoyKBRecipe:
            chosen_size = workflow_size_dict.get(random.randint(1, 3))
        else:
            chosen_size = workflow_size_dict.get(random.randint(1, 5))

        if chosen_Recipe_class == MontageRecipe and chosen_size < 133:
            chosen_size = 133

        # creating a workflow recipe
        recipe = chosen_Recipe_class.from_num_tasks(num_tasks=chosen_size)
        # creating an instance of the workflow generator with the chosen workflow recipe
        generator = WorkflowGenerator(recipe)
        # generating a synthetic workflow trace of the Seismology workflow
        workflow = generator.build_workflow()
        # writing the synthetic workflow trace into a JSON file
        name = "{}_{}_{}.json".format(str(i), chosen_Recipe_class.__name__, str(chosen_size))
        # print(name)
        os.path.join(path, name)
        workflow.write_json(os.path.join(path, name))
        print(i, " generated")
