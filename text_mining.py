# Author:   Koen Rademaker
# Date:     07/06/2017
# Version:  0.4
# Status:   In progress

#   TO-DO LIST
# Set up local SQL Developer database to test insert statements.
# Execute SQL statements to local database with cx_Oracle, including using variables in statements.
# Complete the function save_to_database() which saves (some of) the results from text_retrieval() to the local database.
# Bring all functions together in main().

from Bio import Entrez
Entrez.email = "koenrademaker@outlook.com"
# Report problems with accessing PubMed to this e-mail address.

lox_synonym_list = [["3-LOX", ["3-lipoxygenase", "hydroperoxy icosatetraenoate dehydratase", "epidermal lipoxygenase-3", "hydroperoxy icosatetraenoate isomerase", "lipoxygenase-3", "soybean lipoxygenase-3"]]
,["5-LOX", ["5-lipoxygenase", "arachidonate 5-lipoxygenase", "5DELTA-lipoxygenase", "arachidonic 5-lipoxygenase", "arachidonic acid 5-lipoxygenase", "C-5-lipoxygenase", "DELTA5-lipoxygenase", "lipoxygenase 15", "lipoxygenase 5", "PMNL 5-lipoxygenase"]]
,["8-LOX", ["8-lipoxygenase", "arachidonate 8-lipoxygenase", "8(R)-lipoxygenase", "8R-lipoxygenase", "8S-lipoxygenase", "arachidonic acid C-8 lipoxygenase", "linoleate 8R-lipoxygenase"]]
,["9-LOX", ["9-lipoxygenase", "linoleate 9S-lipoxygenase", "9S-lipoxygenase", "linoleate 9-lipoxygenase", "9R-lipoxygenase", "linolenate 9R-lipoxygenase"]]
,["9/13-LOX", ["9/13-lipoxygenase", "linoleate 9/13-lipoxygenase", "13/9 lipoxygenase", "linoleate 9 S-lipoxygenase", "manganese 9S-lipoxygenase"]]
,["10-LOX", ["10-lipoxygenase", "10R-lipoxygenase", "10S-lipoxygenase"]]
,["11-LOX", ["11-lipoxygenase", "linoleate 11-lipoxygenase", "manganese lipoxygenase"]]
,["12-LOX", ["12-lipoxygenase", "arachidonate 12-lipoxygenase", "(12R)-lipoxygenase", "11R-lipoxygenase", "12(R)-lipoxygenase", "12(S)-lipoxygenase", "12DELTA-lipoxygenase", "12R-lipoxygenase", "12S-lipoxygenase", "2/15-lipoxygenase", "C-12 lipoxygenase", "DELTA 12-lipoxygenase", "epidermal-type lipoxygenase", "human platelet 12-lipoxygenase", "leukocyte-type 12-lipoxygenase", "leukocyte-type 12/15-lipoxygenase", "leukocyte-type lipoxygenase", "lipoxygenase 12", "platelet-type 12(S)-lipoxygenase", "platelet-type 12-human lipoxygenase", "platelet-type 12-lipoxygenase", "Platelet-type lipoxygenase 12"]]
,["12/15-LOX", ["12/15 lipoxygenase", "12/15-lipoxygenases", "12/15-lipoxygenase"]]
,["13-LOX", ["13-lipoxygenase", "linoleate 13S-lipoxygenase", "(13S)-lipoxygenase", "13S-lipoxygenase", "iron 13S-lipoxygenase", "linoleate 13-lipoxygenase"]]
,["15-LOX", ["15-lipoxygenase", "15(S)-lipoxygenase-1", "15-lipoxygenase 1", "15-lipoxygenase 2", "15-lipoxygenase type 1", "15-lipoxygenase type 2", "15-lipoxygenase type-1", "15-lipoxygenase-1", "15-lipoxygenase-2", "15-lipoxygenase-I", "15S-lipoxygenase", "arachidonate 15-lipoxygenase", "arachidonate 15-lipoxygenase-1", "arachidonic acid 15-lipoxygenase", "endothelial 15-lipoxygenase-1", "human prostate epithelial 15-lipoxygenase-2", "linoleic acid omega-6-lipoxygenase", "lipoxygenase L-1", "omega-6 lipoxygenase", "reticulocyte 15-lipoxygenase-1", "reticulocyte-type 15-human lipoxygenase", "reticulocyte-type 15-lipoxygenase", "soybean 15-lipoxygenase"]]]
# Contains a list of synonyms for each LOX to expand the number of results for a PubMed query.
application_list = ["abiotic", "acid precipitation", "active immunity", "active transport", "adaptation", "aerobe", "aggression", "algae chlorophyll", "allele", "allergen", "allergy", "alveoli", "amino acids", "amniotic egg", "amniotic sac", "anaerobe", "angiosperms", "antibiotics", "antibody", "antigen", "anus", "appendages", "application", "artery", "ascus", "asexual reproduction", "asthma", "atmosphere", "atriums", "auxin", "axon", "basidium Club", "behavior", "bilateral symmetry", "binomial nomenclature", "biogenesis", "biological vector", "biomes", "biosphere", "biotic", "bladder", "bleaching", "brain stem", "bronchi", "budding", "cambium", "cancer", "capillary", "carbohydrate", "Carbon cycle", "cardiac muscle", "carnivore", "carrying capacity", "cartilage", "cell", "cell membrane", "cell theory", "cell wall", "cellulose", "central nervous system", "cerebellum", "cerebrum", "chemical digestion", "chemosynthesis", "chemotherapy", "chlorophyll", "chloroplast", "chordate", "chromosome", "chyme", "cilia", "climate", "climax community", "closed circulatory system", "cochlea Fluid", "commensalism", "community", "condensation", "conditioning", "consumer", "contour feathers", "control", "coral reef", "courtship behavior", "crop", "cuticle", "cyclic behavior", "cytoplasm", "day neutral plant", "deciduous forest", "dendrite", "dermis", "desert", "diaphragm", "dicot", "diffusion", "diploid", "DNA", "dominant", "down feathers", "ecology", "ecosystem", "ectotherm", "effect", "egg", "embryo", "embryology", "emphysema", "endocytosis", "endoplasmic reticulum", "endoskeleton", "endospore", "endotherm", "energy pyramid", "enzyme", "epidermis", "equilibrium", "erosion", "estivation", "estuary", "evaporation", "evolution", "exhibits", "exocytosis", "exoskeleton", "fermentation", "fertilization", "fetal stress", "fetus", "fin", "fission", "flagellum", "food group", "food web", "fossil fuels", "free living organism", "frond", "gametophyte stage", "gene", "genetic engineering", "genetics", "genotype", "genus", "geothermal energy", "germination", "gestation period", "gill slits", "gills", "gizzard", "golgi bodies", "gradualism", "grasslands", "greenhouse effect", "guard cells", "gymnosperms", "habitat", "haploid", "hazardous wastes", "hemoglobin", "herbivore", "heredity", "hermaphrodite", "heterozygous", "hibernation", "homeostasis", "hominid",\
                   "homo sapiens", "homologous", "homozygous", "hormone", "host cell", "hybrid", "hydroelectric power", "hyphae", "hypothesis", "immune system", "imprinting", "incomplete dominance", "incubate", "infectous disease ", "inhibits", "innate behavior", "inorganic compound", "insight", "instinct", "intertidal zone", "invertebrate", "involuntary muscle", "joint", "kidney bean", "kingdom", "larynx", "law", "lichen", "ligament", "limiting factor", "long day plant", "lymph", "lymph node", "lymphatic system", "lymphocyte", "mammals", "mammary glands", "mantle", "marsupial", "mechanical digestion", "medusa", "meiosis", "melanin", "menstrual cycle", "nervecord", "neuron", "niche", "nitrogen cycle", "nitrogen fixation", "nitrogen fixing bacteria", "noninfectious disease", "nonrenewable resources", "Nonvascular plant", "notochord", "nuclear energy", "nucleus", "nutrients", "olfactory cell", "omnivore", "open circulatory system", "organ", "organelles", "organic compounds", "organism", "osmosis", "ovary", "ovary", "ovulation", "ovule", "ozone depletion", "parasitism", "passive immunity", "passive transport", "pasteurization", "pathogen", "pathway", "periosteum", "peripheral nervous system", "peristalsis", "petroleum", "pharynx", "phenotype", "pheromone", "phloem", "photoperiodism", "photosynthesis", "phylogeny", "pioneer species", "pistil", "placenta", "placental", "plasma", "platelet", "pollen grain", "pollination", "pollutant", "polygenic inheritance", "polyp", "population", "postanal tail", "preening", "pregnancy", "primates", "producer", "production", "protein", "prothallus", "protist", "protozoan", "pseudopods", "pulmonary circulation", "punctuated equilibrium", "punnett square", "radial symmetry", "radioactive element", "radula", "recessive", "recycling", "reflex", "renewable resources", "respiration", "retina", "rhizoids", "rhizome", "ribosome", "RNA", "role", "saprophyte", "scales", "scientific method", "sedimentary rock", "semen", "sessile", "setae", "sex linked gene", "sexual reproduction", "sexually transmitted disease", "short day plant", "skeletal muscle", "skeletal system", "smooth muscle", "social behavior", "society", "soil", "sori", "species", "sperm", "spiracles", "spontaneous generation", "sporangium", "spore", "spores", "sporophyte stage", "stamen", "stinging cells ", "stomata", "succession", "symbiosis",\
                   "synapse", "systemic circulation", "taiga", "taste bud", "temperate rain forest", "tendon", "tentacles", "testis", "theory", "tissue", "toxin", "trachea", "tropical rain forest", "tropism", "tube feet", "tumor", "tundra", "umbilical  cord", "ureter", "urethra", "urinary system", "urine", "uterus", "vaccination", "vaccine", "vaccine", "vagina", "variable", "variation", "vascular plant", "vein", "ventricles", "vertebrae", "vertebrate", "vestigial structure", "villi", "virus", "vitamin", "voluntary muscle", "water cycle", "water vascular system", "wetland", "xylem", "zygote"]
# Contains a list of biological processes and terms to use during

word_list = []
# Contains all words used during co-occurrence text mining and is used for the visualization of the results.
relation_list = []
# Contains all relations between LOXs and a application based on the results of text mining. The LOX and application are stored as separate items within a list.
count_list = []
# Contains the number of matches found for a relation stored in relation_list. The index used matches the one used in relation_list and both values are used together for visualization.

def text_mining_get_count(query):
    handle = Entrez.egquery(term=query)
    record = Entrez.read(handle)

    for row in record["eGQueryResult"]:
        if row["DbName"] == "pubmed":
            count = int(row["Count"])
    handle.close()
    return count
# Returns the number of results found for a PubMed query based on a given search term.

def text_mining_esearch(query, count):
    handle = Entrez.esearch(db="pubmed", term=query, retmax=count)
    record = Entrez.read(handle)
    temp_id_list = record["IdList"]
    handle.close()

    id_list = []
    for item in temp_id_list:
        id_list.append(int(item))

    return id_list
# Returns the PMID's for a PubMed query based on a given search term.

def text_mining_esummary(PMID):
    handle = Entrez.esummary(db="pubmed", id=PMID)
    record = Entrez.read(handle)

    publication_year = record[0]['PubDate'][0:4]
    temp_author_list = record[0]['AuthorList']
    handle.close()

    author_list = []
    for item in temp_author_list:
        author_list.append(str(item))

    return publication_year, author_list
# Returns the publication year and list of authors for a PubMed article based on a given PMID

def text_mining_efetch(PMID):
    temp_keyword_list = []

    handle = Entrez.efetch(db="pubmed", id=PMID, rettype="pubmed")
    record = handle.read()
    record_list = record.split("\n")
    handle.close()

    for line in record_list:
        if "</Keyword>" in line:
            temp_keyword = line[line.find(">") + 1:line.find("</Keyword>")]
            temp_keyword_list.append(temp_keyword)

    return temp_keyword_list
# Returns the keywords isolated from the abstract of a PubMed article based on a given PMID.

def combine_query(lox, application):
    if application == "":
        temporary_string = "("

        for synonym_item in range(0, len(lox_synonym_list)):
            temporary_lox = lox_synonym_list[synonym_item][0]
            if (lox == temporary_lox):
                temporary_string += '"' + lox + '"' + "*"
                for synonym in range(0, len(lox_synonym_list[synonym_item][1])):
                    temporary_synonym = '"' + lox_synonym_list[synonym_item][1][synonym] + '"'
                    temporary_string += temporary_synonym + "*"

        temporary_string = temporary_string.replace("*", ") OR (")
        temporary_string = temporary_string[:len(temporary_string) - 5]
        temporary_string = "(" + temporary_string + ")"
    else:
        temporary_string = "("

        for synonym_item in range(0, len(lox_synonym_list)):
            temporary_lox = lox_synonym_list[synonym_item][0]
            if (lox == temporary_lox):
                temporary_string += '"' + lox + '"' + "*"
                for synonym in range(0, len(lox_synonym_list[synonym_item][1])):
                    temporary_synonym = '"' + lox_synonym_list[synonym_item][1][synonym] + '"'
                    temporary_string += temporary_synonym + "*"

        temporary_string = temporary_string.replace("*", ") OR (")
        temporary_string = temporary_string[:len(temporary_string) - 5]
        temporary_string = "(" + temporary_string + ")" + " AND " + application

    return temporary_string
# Forms a query that includes all synonyms for a certain LOX to expand the number of results found during co-occurrence text mining.

def text_retrieval():
    for synonym_item in range(0, len(lox_synonym_list)):
    # for synonym_item in range(0, 1):
        keyword = lox_synonym_list[synonym_item][0]
        query = combine_query(keyword, "")
        count = text_mining_get_count(query)

        if (count != 0):
            id_list = text_mining_esearch(query, count)
            # print("COUNT:", count)
            # print("ID LIST:", id_list)
            for article_id in id_list:
                article_year, article_author_list = text_mining_esummary(article_id)
                # print("ARTICLE YEAR:", article_year)
                # print("AUTHOR_LIST:", article_author_list)

                try:
                    article_keyword_list = text_mining_efetch(article_id)
                    # print("KEYWORD LIST:", article_keyword_list)

                    for article_keyword in article_keyword_list:
                        if article_keyword not in application_list:
                            application_list.append(article_keyword)
                except UnicodeDecodeError:
                    print("KEYWORD LIST is empty")
# Loops through all LOXs and associated synonyms and performs text retrieval, returning data such as PubMed ID, a list of authors, year of publication and all keywords found in the article.

def text_analysis():
    for synonym_item in range(0, len(lox_synonym_list)):
        lox_keyword = lox_synonym_list[synonym_item][0]
        for application in application_list:
            query = combine_query(lox_keyword, application)
            count = text_mining_get_count(query)
            if count > 0:
                # print("--DEBUG-- Results found for", lox_keyword, "with", application)
                relation_list.append([lox_keyword, application])
                count_list.append(count)
# Loops through all LOXs and associated synonyms and all known applications and performs text analysis, returning relations found between LOXs and applications and the number of relations.
