require 'spec_helper'

RSpec.describe Solver do
  subject { described_class.new.call(arr) }

  context "Test case 1" do
    let(:arr) { [1, 2, 3, 4, 5] }
    let(:expected_output) { [120, 60, 40, 30, 24] }

    it { is_expected.to eq(expected_output) }
  end

  context "Test case 2" do
    let(:arr) { [3, 2, 1] }
    let(:expected_output) { [2, 3, 6] }

    it { is_expected.to eq(expected_output) }
  end

  context "Test case 3" do
    let(:arr) { [100] }
    let(:expected_output) { [1] }

    it { is_expected.to eq(expected_output) }
  end

  context "Test case 4" do
    let(:arr) { [] }
    let(:expected_output) { [] }

    it { is_expected.to eq(expected_output) }
  end
end
