require 'spec_helper'

RSpec.describe Solver do
  subject { described_class.new.call(arr) }

  context "Test case 1" do
    let(:arr) { [1, 4, 3, 9, 10, 13, 7] }
    let(:expected_result) { [1, 3, 13] }

    it { is_expected.to eq(expected_result) }
  end

  context "Test case 2" do
    let(:arr) { [0, 2, 8, 5, 2, 1, 4, 13, 23] }
    let(:expected_result) { [0, 2, 8, 5, 2, 1, 13] }

    it { is_expected.to eq(expected_result) }
  end

  context "Test case 3" do
    let(:arr) { (50..1000).to_a }
    let(:expected_result) { [55, 89, 144, 233, 377, 610, 987] }

    it { is_expected.to eq(expected_result) }
  end

  context "Test case 4" do
    let(:arr) { [] }
    let(:expected_result) { [] }

    it { is_expected.to eq(expected_result) }
  end
end
