import storingwebpages
import trials
import unifier
import cleaner
query = "husband"
number_of_files = 200
storingwebpages.results(query, "advanced", "1674", "00", "1913", "99", number_of_files)

trials.trials(query, number_of_files)

unifier.unifier(query, number_of_files)

cleaner.cleaner(query, number_of_files)
