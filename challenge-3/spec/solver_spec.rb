require 'spec_helper'

RSpec.describe Solver do
  subject { described_class.new.call(arr, k) }

  context "Test case 1" do
    let(:arr) { [10, 15, 3, 7] }
    let(:k) { 17 }

    it { is_expected.to be true }
  end

  context "Test case 2" do
    let(:arr) { [10, 15, 3, 7] }
    let(:k) { 11 }

    it { is_expected.to be false }
  end

  context "with duplicated values" do
    let(:arr) { [1, 2, 3, 2, 1] }
    let(:k) { 5 }

    it { is_expected.to be true }
  end

  context "with empty array" do
    let(:arr) { [] }
    let(:k) { 10 }

    it { is_expected.to be false }
  end
end
