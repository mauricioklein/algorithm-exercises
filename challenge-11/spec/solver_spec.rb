require 'spec_helper'

RSpec.describe Solver do
  subject { described_class.new.call(ternary_if) }

  describe "Test case #1" do
    let(:ternary_if) { "a?b:c" }
    let(:expected_output) { "(( < b > ) < a > ( < c > ))" }

    it { is_expected.to eq(expected_output) }
  end

  describe "Test case #2" do
    let(:ternary_if) { "a?b?c:d:e" }
    let(:expected_output) { "((( < c > ) < b > ( < d > )) < a > ( < e > ))" }

    it { is_expected.to eq(expected_output) }
  end
end
