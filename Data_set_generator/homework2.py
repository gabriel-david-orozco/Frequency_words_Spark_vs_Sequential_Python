import storingwebpages
import trials
import unifier
import cleaner
query = "husband"
storingwebpages.results(query, "advanced", "1674", "00", "1913", "99", 20000)

trials.trials(query)

unifier.unifier(query)

cleaner.cleaner(query)
