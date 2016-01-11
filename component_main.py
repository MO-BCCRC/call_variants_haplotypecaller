'''
Created on Sep 10, 2014

@author: raniba
'''

import os
from kronos.utils import ComponentAbstract


class Component(ComponentAbstract):

    '''
    GATK HaplotypeCaller : Call SNPs and indels simultaneously via local re-assembly of haplotypes in an active region.
    '''
    def __init__(self, component_name='cvh', component_parent_dir=None, seed_dir=None):
       self.version = "0.0.1"

        ## initialize ComponentAbstract
       super(Component, self).__init__(component_name, component_parent_dir, seed_dir)

    def make_cmd(self, chunk=None):
        '''
        GATK HaplotypeCaller
        '''

        java_mem = '-Xmx3072M'
        java_jar_option = '-jar'
        cvh_jar = self.requirements['gatk']
        cvh_infile = self.args.infile
        cvh_outfile = self.args.outfile
        cvh_ref_genome = self.args.ref_genome

        cmd = self.requirements['java']
        cmd_args = [java_mem,
                    java_jar_option,
                    cvh_jar,
                    "-T", "HaplotypeCaller",
                    "-R", cvh_ref_genome,
                    "-I", cvh_infile,
                    "-o", cvh_outfile,
                    "-stand_call_conf", 30,
                    "-stand_emit_conf", 10,
                    "-minPruning", 3]

        return cmd, cmd_args


# to run as stand alone
def _main():
    '''main function'''
    cvh_post = Component()
    cvh_post.args = component_ui.args
    cvh_post.run()

if __name__ == '__main__':

    import component_ui

    _main()
