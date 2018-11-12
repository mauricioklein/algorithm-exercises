require 'spec_helper'

RSpec.describe Solver do
  subject { described_class.new.call(input) }

  describe "Test case #1" do
    let(:input) { "AC2BEW3" }
    let(:expected_output) { "ABCEW5" }

    it { is_expected.to eq(expected_output) }
  end

  describe "Test case #2" do
    let(:input) { "ABAC1D4" }
    let(:expected_output) { "AABCD5" }

    it { is_expected.to eq(expected_output) }
  end

  describe "Test case #3" do
    let(:input) { "ABABCD" }
    let(:expected_output) { "AABBCD0" }

    it { is_expected.to eq(expected_output) }
  end

  describe "Test case #4" do
    let(:input) { "244" }
    let(:expected_output) { "10" }

    it { is_expected.to eq(expected_output) }
  end

  describe "Test case #5" do
    let(:input) { "" }
    let(:expected_output) { "0" }

    it { is_expected.to eq(expected_output) }
  end
end
