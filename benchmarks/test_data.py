from qiime_default_reference import get_template_alignment, get_reference_sequences

from skbio import SequenceCollection

gapped_sequences = [(s.id, str(s)) for s in SequenceCollection.read(get_template_alignment())][:100]

sequences = [(s.id, str(s)) for s in SequenceCollection.read(get_reference_sequences())][:100]
